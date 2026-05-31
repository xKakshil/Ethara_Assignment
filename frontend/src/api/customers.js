import apiClient from "./axios";

export async function getCustomers() {
  const response = await apiClient.get(
    "/customers"
  );

  return response.data;
}

export async function createCustomer(
  customerData
) {
  const response = await apiClient.post(
    "/customers",
    customerData
  );

  return response.data;
}

export async function deleteCustomer(
  customerId
) {
  await apiClient.delete(
    `/customers/${customerId}`
  );
}