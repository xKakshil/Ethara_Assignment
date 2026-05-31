import apiClient from "./axios";

export async function getDashboard() {
  const response =
    await apiClient.get(
      "/dashboard"
    );

  return response.data;
}