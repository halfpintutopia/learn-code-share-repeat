import React, { useState } from "react";

const UseStateWithObjects = () => {
  const [name, setName] = useState({ firstName: "", lastName: "" });

  const handleChange = (setter) => (e) => {
    const { name, value } = e.target;
    setter((prevState) => ({ ...prevState, [name]: value }));
  };

  return (
    <div>
      <form>
        <input
          name="firstName"
          type="text"
          value={name.firstName}
          onChange={handleChange(setName)}
        />
        <input
          name="lastName"
          type="text"
          value={name.lastName}
          onChange={handleChange(setName)}
        />
        <h2>{JSON.stringify(name)}</h2>
      </form>
    </div>
  );
};

export default UseStateWithObjects;
