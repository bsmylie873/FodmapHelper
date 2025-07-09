import React from 'react';

const About: React.FC = () => {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">About FODMAP Helper</h1>
      
      <section className="mb-8">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">What is FODMAP Helper?</h2>
        <p className="text-gray-600 mb-4">
          FODMAP Helper is a comprehensive tool designed to assist people following the low FODMAP diet.
          Our database provides detailed information about the FODMAP content of various foods,
          helping you make informed decisions about your diet.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">How to Use</h2>
        <ul className="list-disc list-inside text-gray-600 space-y-2">
          <li>Browse our food database by category</li>
          <li>Search for specific foods</li>
          <li>Check FODMAP levels for different serving sizes</li>
          <li>Find alternative food options</li>
        </ul>
      </section>

      <section className="mb-8">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Disclaimer</h2>
        <p className="text-gray-600 mb-4">
          The information provided by FODMAP Helper is for informational purposes only and is not
          intended to be a substitute for professional medical advice, diagnosis, or treatment.
          Always seek the advice of your physician or other qualified health provider with any
          questions you may have regarding a medical condition.
        </p>
      </section>

      <section>
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Contact & Support</h2>
        <p className="text-gray-600">
          For questions, feedback, or support, please visit our GitHub repository or contact us
          through our support channels.
        </p>
      </section>
    </div>
  );
};

export default About; 