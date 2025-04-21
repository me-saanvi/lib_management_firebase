const formContainer = document.getElementById("formContainer");
const output = document.getElementById("output");

const operations = {
  addBook: ["Book ID", "Title", "Author", "Published Year", "Genre"],
  deleteBook: ["Book ID"],
  displayBooks: [],
  searchBook: ["Title Keyword"],
  addUser: ["User ID", "Username", "Email"],
  deleteUser: ["User ID"],
  showUsers: [],
  searchUser: ["Field (username/email)", "Value"],
  updateUser: ["User ID", "Field", "New Value"],
  borrowBook: ["User ID", "Book ID", "Duration (days)"],
  returnBook: ["User ID", "Book ID"],
  showBorrowed: ["User ID"],
  updateBook: ["Book ID", "Field", "New Value"]
};

document.getElementById("operationSelect").addEventListener("change", function () {
  const selected = this.value;
  formContainer.innerHTML = "";

  if (!selected) return;

  const fields = operations[selected];
  const form = document.createElement("form");

  fields.forEach((labelText, i) => {
    const input = document.createElement("input");
    input.type = "text";
    input.placeholder = labelText;
    input.name = `field${i}`;
    form.appendChild(input);
    form.appendChild(document.createElement("br"));
  });

  const submit = document.createElement("button");
  submit.textContent = "Submit";
  submit.type = "submit";
  form.appendChild(submit);

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const values = Array.from(form.elements)
      .filter((el) => el.name && el.value)
      .map((el) => el.value);

    const endpointMap = {
      addBook: "add_book",
      deleteBook: "delete_book",
      displayBooks: "show_books",
      searchBook: "search_book",
      addUser: "add_user",
      deleteUser: "delete_user",
      showUsers: "show_users",
      searchUser: "search_user",
      updateUser: "update_user",
      borrowBook: "borrow_book",
      returnBook: "return_book",
      showBorrowed: "show_borrow",
      updateBook: "update_book"
    };

    const endpoint = endpointMap[selected];
    if (!endpoint) {
      output.textContent = "❌ Invalid operation selected!";
      return;
    }

    try {
      const method = selected === "displayBooks" || selected === "showUsers" || selected === "showBorrowed"
        ? "GET"
        : "POST";

      const url = `http://127.0.0.1:5000/${endpoint}`;

      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: method === "POST" ? JSON.stringify({ values }) : null
      });

      const data = await res.json();
      output.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
      output.textContent = "❌ Error connecting to backend: " + err.message;
    }
  });

  formContainer.appendChild(form);
});

