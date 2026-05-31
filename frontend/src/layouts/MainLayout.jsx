import {
  Outlet,
  NavLink,
} from "react-router-dom";

export default function MainLayout() {
  const linkClass = ({ isActive }) =>
  `
  block
  px-5
  py-4
  rounded-xl
  font-medium
  transition-all
  duration-200
  ${
    isActive
      ? "bg-blue-600 text-white shadow-lg"
      : "text-slate-300 hover:bg-slate-800 hover:text-white"
  }
`;

  return (
    <div className="flex min-h-screen">
      <aside
        className="
          w-72
          bg-slate-950
          shadow-2xl
          text-white
          p-6
        "
      >
        <h1
          className="
            text-3xl
            font-extrabold
            mb-12
            tracking-tight
          "
        >
          Inventory System
        </h1>

        <nav className="space-y-2">
          <NavLink
            to="/"
            className={linkClass}
          >
            Dashboard
          </NavLink>

          <NavLink
            to="/products"
            className={linkClass}
          >
            Products
          </NavLink>

          <NavLink
            to="/customers"
            className={linkClass}
          >
            Customers
          </NavLink>

          <NavLink
            to="/orders"
            className={linkClass}
          >
            Orders
          </NavLink>
        </nav>
      </aside>

      <main
        className="
          flex-1
          bg-slate-50
          p-8
        "
      >
        <Outlet />
      </main>
    </div>
  );
}