import { useEffect, useState } from "react";

import {
  getCustomers,
  createCustomer,
  deleteCustomer,
} from "../api/customers";

export default function CustomersPage() {
  const [customers, setCustomers] =
    useState([]);

  const [formData, setFormData] =
    useState({
      full_name: "",
      email: "",
      phone: "",
    });

  async function loadCustomers() {
    try {
      const data =
        await getCustomers();

      setCustomers(data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadCustomers();
  }, []);

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      await createCustomer(formData);

      setFormData({
        full_name: "",
        email: "",
        phone: "",
      });

      await loadCustomers();
    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
          "Failed to create customer"
      );
    }
  }

  async function handleDelete(id) {
    if (
      !window.confirm(
        "Delete customer?"
      )
    ) {
      return;
    }

    try {
      await deleteCustomer(id);

      await loadCustomers();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <h1
        className="
          text-5xl 
          font-bold 
          tracking-tight
          mb-6
        "
      >
        Customers
      </h1>

      <form
        onSubmit={handleSubmit}
        className="
          bg-white
p-8
rounded-2xl
shadow-lg
border
border-slate-200
          mb-8
        "
      >
        <div
          className="
            grid
            md:grid-cols-3
            gap-4
          "
        >
          <input
            placeholder="Full Name"
            value={formData.full_name}
            onChange={(e) =>
              setFormData({
                ...formData,
                full_name:
                  e.target.value,
              })
            }
            className="
              border
              p-3
              rounded-lg
            "
            required
          />

          <input
            placeholder="Email"
            type="email"
            value={formData.email}
            onChange={(e) =>
              setFormData({
                ...formData,
                email:
                  e.target.value,
              })
            }
            className="
              border
              p-3
              rounded-lg
            "
            required
          />

          <input
            placeholder="Phone"
            value={formData.phone}
            onChange={(e) =>
              setFormData({
                ...formData,
                phone:
                  e.target.value,
              })
            }
            className="
              border
              p-3
              rounded-lg
            "
          />
        </div>

        <button
          type="submit"
          className="
            mt-4
            bg-green-600
            hover:bg-green-700
            transition
            text-white
            px-5
            py-3
            rounded-lg
          "
        >
          Add Customer
        </button>
      </form>

      <div
        className="
          bg-white
rounded-2xl
shadow-lg
border
border-slate-200
          overflow-hidden
        "
      >
        <table
          className="
            w-full
          "
        >
          <thead
            className="
              bg-slate-100
            "
          >
            <tr>
              <th className="p-4 text-left">
                Name
              </th>

              <th className="p-4 text-left">
                Email
              </th>

              <th className="p-4 text-left">
                Phone
              </th>

              <th className="p-4 text-left">
                Actions
              </th>
            </tr>
          </thead>

          <tbody>
            {customers.map(
              (customer) => (
                <tr
                  key={customer.id}
                  className="
                    border-t
hover:bg-slate-50
transition
                  "
                >
                  <td className="p-4">
                    {
                      customer.full_name
                    }
                  </td>

                  <td className="p-4">
                    {customer.email}
                  </td>

                  <td className="p-4">
                    {customer.phone}
                  </td>

                  <td className="p-4">
                    <button
                      onClick={() =>
                        handleDelete(
                          customer.id
                        )
                      }
                      className="
                        bg-red-500
                        text-white
                        px-3
                        py-1
                        rounded
                      "
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              )
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}