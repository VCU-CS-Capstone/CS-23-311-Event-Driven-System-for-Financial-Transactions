import React from 'react';
import { Container } from 'react-bootstrap';
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';
import CreateCustomerForm from './CreateCustomerForm';

const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_PUBLISHABLE_KEY);

const App = () => {
  return (
    <Container>
      <h1>Stripe Payment Form</h1>
      <Elements stripe={stripePromise}>
        <CreateCustomerForm />
      </Elements>
    </Container>
  );
};

export default App;
