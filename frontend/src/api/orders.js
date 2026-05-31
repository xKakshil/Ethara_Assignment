import apiClient from "./axios";

export async function getOrders() {
  const response = await apiClient.get(
    "/orders"
  );

  return response.data;
}

export async function createOrder(
  orderData
) {
  const response = await apiClient.post(
    "/orders",
    orderData
  );

  return response.data;
}

export async function deleteOrder(
  orderId
) {
  await apiClient.delete(
    `/orders/${orderId}`
  );
}