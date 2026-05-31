import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import DashboardPage from "../pages/DashboardPage";
import ProductsPage from "../pages/ProductsPage";
import CustomersPage from "../pages/CustomersPage";
import OrdersPage from "../pages/OrdersPage";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route
            path="/"
            element={<DashboardPage />}
          />

          <Route
            path="/products"
            element={<ProductsPage />}
          />

          <Route
            path="/customers"
            element={<CustomersPage />}
          />

          <Route
            path="/orders"
            element={<OrdersPage />}
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}