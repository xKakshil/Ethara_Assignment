import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import MainLayout
  from "../layouts/MainLayout";

import DashboardPage
  from "../pages/DashboardPage";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        <Route
          element={
            <MainLayout />
          }
        >
          <Route
            path="/"
            element={
              <DashboardPage />
            }
          />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}