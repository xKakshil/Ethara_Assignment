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
    text-center
    ${
      isActive
        ? "bg-blue-600 text-white shadow-lg"
        : "text-slate-300 hover:bg-slate-800 hover:text-white"
    }
  `;


  return (
    <div
      className="
        flex
        min-h-screen

        md:flex-row
        flex-col
      "
    >

      {/* SIDEBAR */}
      <aside
        className="
          bg-slate-950
          shadow-2xl
          text-white

          w-72
          p-6

          md:min-h-screen

          max-md:w-full
          max-md:h-auto
          max-md:p-5
        "
      >

        <h1
          className="
            text-3xl
            font-extrabold
            tracking-tight

            mb-12

            max-md:text-2xl
            max-md:mb-6
          "
        >
          Inventory System
        </h1>


        <nav
          className="
            space-y-2

            max-md:space-y-0
            max-md:grid
            max-md:grid-cols-2
            max-md:gap-3
          "
        >

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


      {/* CONTENT */}
      <main
        className="
          flex-1
          bg-slate-50

          p-8

          max-md:p-5
          max-md:w-full
        "
      >

        <Outlet />

      </main>

    </div>
  );
}
