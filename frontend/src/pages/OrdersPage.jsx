import { useEffect, useState } from "react";

import {
  getOrders,
  createOrder,
  deleteOrder,
} from "../api/orders";

import {
  getProducts,
} from "../api/products";

import {
  getCustomers,
} from "../api/customers";

export default function OrdersPage() {
  const [orders, setOrders] =
    useState([]);

  const [products, setProducts] =
    useState([]);

  const [customers, setCustomers] =
    useState([]);

  const [customerId, setCustomerId] =
    useState("");

  const [productId, setProductId] =
    useState("");

  const [quantity, setQuantity] =
    useState(1);

  async function loadData() {
    try {
      const [
        orderData,
        productData,
        customerData,
      ] = await Promise.all([
        getOrders(),
        getProducts(),
        getCustomers(),
      ]);

      setOrders(orderData);
      setProducts(productData);
      setCustomers(customerData);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  const customerMap =
    Object.fromEntries(
      customers.map(
        (customer) => [
          customer.id,
          customer.full_name,
        ]
      )
    );

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      await createOrder({
        customer_id: customerId,
        items: [
          {
            product_id:
              productId,
            quantity:
              Number(quantity),
          },
        ],
      });

      setCustomerId("");
      setProductId("");
      setQuantity(1);

      await loadData();
    } catch (error) {
      console.error(error);

      alert(
        error.response?.data
          ?.detail ||
          "Failed to create order"
      );
    }
  }

  async function handleDelete(
    id
  ) {
    if (
      !window.confirm(
        "Delete order?"
      )
    ) {
      return;
    }

    try {
      await deleteOrder(id);

      await loadData();
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
        Orders
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
          <select
            value={customerId}
            onChange={(e) =>
              setCustomerId(
                e.target.value
              )
            }
            className="
              border
              p-3
              rounded-lg
            "
            required
          >
            <option value="">
              Select Customer
            </option>

            {customers.map(
              (customer) => (
                <option
                  key={customer.id}
                  value={
                    customer.id
                  }
                >
                  {
                    customer.full_name
                  }
                </option>
              )
            )}
          </select>

          <select
            value={productId}
            onChange={(e) =>
              setProductId(
                e.target.value
              )
            }
            className="
              border
              p-3
              rounded-lg
            "
            required
          >
            <option value="">
              Select Product
            </option>

            {products.map(
              (product) => (
                <option
                  key={product.id}
                  value={
                    product.id
                  }
                >
                  {product.name}
                  {" "}
                  (
                  {
                    product.stock_quantity
                  }
                  )
                </option>
              )
            )}
          </select>

          <input
            type="number"
            min="1"
            value={quantity}
            onChange={(e) =>
              setQuantity(
                e.target.value
              )
            }
            className="
              border
              p-3
              rounded-lg
            "
            required
          />
        </div>

        <button
          type="submit"
          className="
            mt-4
            bg-purple-600
hover:bg-purple-700
transition
            text-white
            px-5
            py-3
            rounded-lg
          "
        >
          Create Order
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
                Order ID
              </th>

              <th className="p-4 text-left">
                Customer
              </th>

              <th className="p-4 text-left">
                Total
              </th>

              <th className="p-4 text-left">
                Date
              </th>

              <th className="p-4 text-left">
                Actions
              </th>
            </tr>
          </thead>

          <tbody>
            {orders.map(
              (order) => (
                <tr
                  key={
                    order.id
                  }
                  className="
                    border-t
hover:bg-slate-50
transition
                  "
                >
                  <td className="p-4">
                    {order.id.slice(
                      0,
                      8
                    )}
                  </td>

                  <td className="p-4">
                    {customerMap[
                      order.customer_id
                    ] ||
                      "Unknown Customer"}
                  </td>

                  <td className="p-4">
                    ₹
                    {Number(
                      order.total_amount
                    ).toLocaleString()}
                  </td>

                  <td className="p-4">
                    {new Date(
                      order.created_at
                    ).toLocaleDateString()}
                  </td>

                  <td className="p-4">
                    <button
                      onClick={() =>
                        handleDelete(
                          order.id
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