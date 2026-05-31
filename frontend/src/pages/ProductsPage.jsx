import { useEffect, useState } from "react";

import {
  getProducts,
  createProduct,
  deleteProduct,
} from "../api/products";

export default function ProductsPage() {
  const [products, setProducts] =
    useState([]);

  const [formData, setFormData] =
    useState({
      name: "",
      sku: "",
      description: "",
      price: "",
      stock_quantity: "",
    });

  async function loadProducts() {
    try {
      const data =
        await getProducts();

      setProducts(data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadProducts();
  }, []);

  async function handleSubmit(
    event
  ) {
    event.preventDefault();

    try {
      await createProduct({
        ...formData,
        price: Number(
          formData.price
        ),
        stock_quantity: Number(
          formData.stock_quantity
        ),
      });

      setFormData({
        name: "",
        sku: "",
        description: "",
        price: "",
        stock_quantity: "",
      });

      await loadProducts();
    } catch (error) {
      console.error(error);
      alert(
        error.response?.data?.detail ||
          "Failed to create product"
      );
    }
  }

  async function handleDelete(id) {
    if (
      !window.confirm(
        "Delete this product?"
      )
    ) {
      return;
    }

    try {
      await deleteProduct(id);

      await loadProducts();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <h1
        className="
          text-5xl font-bold tracking-tight
        "
      >
        Products
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
            grid-cols-2
            gap-4
          "
        >
          <input
            type="text"
            placeholder="Name"
            value={formData.name}
            onChange={(e) =>
              setFormData({
                ...formData,
                name: e.target.value,
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
            type="text"
            placeholder="SKU"
            value={formData.sku}
            onChange={(e) =>
              setFormData({
                ...formData,
                sku: e.target.value,
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
            type="number"
            placeholder="Price"
            value={formData.price}
            onChange={(e) =>
              setFormData({
                ...formData,
                price: e.target.value,
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
            type="number"
            placeholder="Stock"
            value={
              formData.stock_quantity
            }
            onChange={(e) =>
              setFormData({
                ...formData,
                stock_quantity:
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

          <textarea
            placeholder="Description"
            value={
              formData.description
            }
            onChange={(e) =>
              setFormData({
                ...formData,
                description:
                  e.target.value,
              })
            }
            className="
              border
              p-3
              rounded-lg
              col-span-2
            "
          />
        </div>

        <button
          type="submit"
          className="
mt-6
bg-blue-600
hover:bg-blue-700
text-white
font-medium
px-6
py-3
rounded-xl
transition
"
        >
          Add Product
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
        <table className="w-full">
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
                SKU
              </th>

              <th className="p-4 text-left">
                Price
              </th>

              <th className="p-4 text-left">
                Stock
              </th>

              <th className="p-4 text-left">
                Actions
              </th>
            </tr>
          </thead>

          <tbody>
            {products.map(
              (product) => (
                <tr
                  key={product.id}
                  className="
border-t
hover:bg-slate-50
transition
"
                >
                  <td className="p-4">
                    {product.name}
                  </td>

                  <td className="p-4">
                    {product.sku}
                  </td>

                  <td className="p-4">
                    ₹{Number(product.price).toLocaleString()}
                  </td>

                  <td className="p-4">
                    {
                      product.stock_quantity
                    }
                  </td>

                  <td className="p-4">
                    <button
                      onClick={() =>
                        handleDelete(
                          product.id
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