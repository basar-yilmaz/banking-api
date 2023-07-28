document.addEventListener("DOMContentLoaded", function () {
  // Fetch and populate the customer list
  fetch("/customers/")
    .then((response) => response.json())
    .then((data) => {
      const customersList = document.getElementById("customersList");
      data.forEach((customer) => {
        const listItem = document.createElement("li");
        const subColumnsDiv = document.createElement("div");
        subColumnsDiv.classList.add("sub-columns");

        const customerIdDiv = document.createElement("div");
        customerIdDiv.classList.add("sub-column");
        customerIdDiv.textContent = `ID: ${customer.id}`;

        const customerNameDiv = document.createElement("div");
        customerNameDiv.classList.add("sub-column");
        customerNameDiv.textContent = `Name: ${customer.name}`;

        subColumnsDiv.appendChild(customerIdDiv);
        subColumnsDiv.appendChild(customerNameDiv);
        listItem.appendChild(subColumnsDiv);

        customersList.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  // Fetch and populate the bank accounts list with balances and owners (customer IDs)
  fetch("/bankaccounts/")
    .then((response) => response.json())
    .then((data) => {
      const bankAccountsList = document.getElementById("bankAccountsList");
      const sourceAccountSelect = document.getElementById("sourceAccount");
      const destinationAccountSelect =
        document.getElementById("destinationAccount");

      data.forEach((account) => {
        const listItem = document.createElement("li");
        const subColumnsDiv = document.createElement("div");
        subColumnsDiv.classList.add("sub-columns");

        const accountNumberDiv = document.createElement("div");
        accountNumberDiv.classList.add("sub-column");
        accountNumberDiv.textContent = `Account Number: ${account.account_id}`;

        const balanceDiv = document.createElement("div");
        balanceDiv.classList.add("sub-column");
        balanceDiv.textContent = `Balance: $${account.balance}`;

        const ownerDiv = document.createElement("div");
        ownerDiv.classList.add("sub-column");
        ownerDiv.textContent = `Owner (Customer ID): ${account.customer}`;

        subColumnsDiv.appendChild(accountNumberDiv);
        subColumnsDiv.appendChild(balanceDiv);
        subColumnsDiv.appendChild(ownerDiv);
        listItem.appendChild(subColumnsDiv);

        bankAccountsList.appendChild(listItem);

        // Create options for source and destination account select boxes
        const sourceOption = document.createElement("option");
        sourceOption.value = account.account_id;
        sourceOption.textContent = `Account Number: ${account.account_id} | Balance: $${account.balance}`;
        sourceAccountSelect.appendChild(sourceOption);

        const destinationOption = document.createElement("option");
        destinationOption.value = account.account_id;
        destinationOption.textContent = `Account Number: ${account.account_id} | Balance: $${account.balance}`;
        destinationAccountSelect.appendChild(destinationOption);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  // Transaction function to handle form submission
  document.getElementById("transferForm").onsubmit = function (event) {
    event.preventDefault();
    const sourceAccount = document.getElementById("sourceAccount").value;
    const destinationAccount =
      document.getElementById("destinationAccount").value;
    const amount = document.getElementById("amount").value;

    const data = {
      source_account_number: sourceAccount,
      destination_account_number: destinationAccount,
      transfer_amount: amount,
    };

    fetch("/transactions/transfer/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        const messageContainer = document.getElementById("messageContainer");
        if (data.message) {
          messageContainer.innerHTML = `<p id="message">${data.message}</p><i id="icon" class="fas fa-check-circle"></i>`;
          messageContainer.classList.remove("error");
          messageContainer.classList.add("success");
        } else if (data.error) {
          messageContainer.innerHTML = `<p id="message">Error: ${data.error}</p><i id="icon" class="fas fa-exclamation-circle"></i>`;
          messageContainer.classList.remove("success");
          messageContainer.classList.add("error");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
