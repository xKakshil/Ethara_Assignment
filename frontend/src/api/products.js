import apiClient from "./axios";

export async function getProducts() {
  const response = await apiClient.get(
    "/products"
  );

  return response.data;
}

export async function createProduct(
  productData
) {
  const response = await apiClient.post(
    "/products",
    productData
  );

  return response.data;
}

export async function deleteProduct(
  productId
) {
  await apiClient.delete(
    `/products/${productId}`
  );
}