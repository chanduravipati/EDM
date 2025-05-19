document.getElementById("consultationForm").addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent default form submission

  // Gather form data
  const formData = {
    firstName: document.getElementById("firstName").value,
    contactNumber: document.getElementById("contactNumber").value,
    village: document.getElementById("village").value,
    email: document.getElementById("email").value,
    issue: document.getElementById("issue").value,
  };

  // Store the data in localStorage
  localStorage.setItem("consultationData", JSON.stringify(formData));

  // Redirect to result.html
  window.location.href = "result.html";
});
