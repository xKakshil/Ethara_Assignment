import { useEffect, useState } from "react";
import { getDashboard } from "../api/dashboard";

export default function DashboardPage() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const result =
          await getDashboard();

        setData(result);
      } catch (error) {
        console.error(error);
      }
    }

    loadDashboard();
  }, []);

  if (!data) {
    return (
      <div className="text-lg">
        Loading dashboard...
      </div>
    );
  }

  return (
    <div>
      <h1
        className="
          text-5xl
          font-bold
          tracking-tight
          mb-8
        "
      >
        Dashboard
      </h1>

      <div
        className="
          grid
          grid-cols-1
          md:grid-cols-3
          gap-6
          mb-8
        "
      >
        <div
          className=" 
            bg-white
            rounded-2xl
            shadow-lg
            border
            border-slate-200
            p-8
            hover:shadow-xl
            transition
          "
        >
          <p className="text-gray-500">
            Total Products
          </p>

          <h2
            className="
              text-6xl
              font-extrabold
              mt-2
            "
          >
            {data.total_products}
          </h2>
        </div>

        <div
          className="
            bg-white
            rounded-2xl
            shadow-lg
            border
            border-slate-200
            p-8
          "
        >
          <p className="text-gray-500">
            Total Customers
          </p>

          <h2
            className="
              text-4xl
              font-bold
              mt-2
            "
          >
            {data.total_customers}
          </h2>
        </div>

        <div
          className="
            bg-white
            rounded-xl
            shadow
            p-6
          "
        >
          <p className="text-gray-500">
            Total Orders
          </p>

          <h2
            className="
              text-4xl
              font-bold
              mt-2
            "
          >
            {data.total_orders}
          </h2>
        </div>
      </div>

      <div
        className="
          bg-white
          rounded-xl
          shadow
          p-6
        "
      >
        <h2
          className="
            text-2xl
            font-semibold
            mb-4
          "
        >
          Low Stock Products
        </h2>

        <table
          className="
            w-full
          "
        >
          <thead>
            <tr
              className="
                border-b
              "
            >
              <th
                className="
                  text-left
                  p-3
                "
              >
                Product
              </th>

              <th
                className="
                  text-left
                  p-3
                "
              >
                Stock
              </th>
            </tr>
          </thead>

          <tbody>
            {data.low_stock_products
              .length === 0 ? (
              <tr>
                <td
                  colSpan="2"
                  className="
                    p-4
                    text-center
                  "
                >
                  No low stock items
                </td>
              </tr>
            ) : (
              data.low_stock_products.map(
                (product) => (
                  <tr
                    key={product.id}
                    className="
                      border-b
                    "
                  >
                    <td className="p-3">
                      {product.name}
                    </td>

                    <td className="p-3">
                      {
                        product.stock_quantity
                      }
                    </td>
                  </tr>
                )
              )
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}