import { useState } from "react";
import { loadStripe } from "@stripe/stripe-js";
import "./CreateCustomerForm.css";


  var pKey = 'pk_test_51MZIy7IgVGXxDnG3Cxl7eJKHdulcV032IzWqXn7ATx3snp6SXetoY7ivH3fEGjZiPcMoVLpIwAmQawcMR94Xpe2q00FxBCDbqF';
  console.log(typeof pKey)
  const stripe = loadStripe(pKey);
  console.log(stripe)

const CreateCustomerForm = () => {
  const [fullName, setFullName] = useState("");
  console.log('hello')
  const [dob, setDob] = useState("");
  const [ssn, setSsn] = useState("");
  const [address, setAddress] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  console.log("hello 2")

  const handleChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case "fullName":
        setFullName(value);
        break;
      case "dob":
        setDob(value);
        break;
      case "ssn":
        setSsn(value);
        break;
      case "address":
        setAddress(value);
        break;
      case "phone":
        setPhone(value);
        break;
      case "email":
        setEmail(value);
        break;
      default:
        break;
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      console.log(fullName);
      const customer = await stripe.customers.create({
        name: fullName,
        email: email,
        address: {
          line1: address,
        },
        phone: phone
      });

      setSuccessMessage("Customer created successfully!");
      console.log(customer.id);
    } catch (error) {
      setErrorMessage(error.message);
      console.error(error);

    }
  };

  return (
    <div className="form-container">
      <h2>Create a New Customer</h2>
      {successMessage && <p className="success-message">{successMessage}</p>}
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label htmlFor="fullName" className="input-label">
          Full Name:
          <input type="text" name="fullName" value={fullName} onChange={handleChange} required />
        </label>
        <label htmlFor="dob" className="input-label">
          Date of Birth:
          <input type="date" name="dob" value={dob} onChange={handleChange} required />
        </label>
        <label htmlFor="ssn" className="input-label">
          Social Security Number:
          <input type="text" name="ssn" value={ssn} onChange={handleChange} required />
        </label>
        <label htmlFor="address" className="input-label">
          Address:
          <input type="text" name="address" value={address} onChange={handleChange} required />
        </label>
        <label htmlFor="phone" className="input-label">
          Phone Number:
          <input type="tel" name="phone" value={phone} onChange={handleChange} required />
        </label>
        <label htmlFor="email" className="input-label">
          Email Address:
          <input type="email" name="email" value={email} onChange={handleChange} required />
        </label>
        <button type="submit">Create Customer</button>
      </form>
    </div>
  );
};

export default CreateCustomerForm;
  