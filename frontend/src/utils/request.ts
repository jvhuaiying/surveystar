import axios from "axios";
import router from "@/router";
import { useAccountStore } from "@/stores/account";

const instance = axios.create({
  baseURL: "/api",
});

instance.interceptors.request.use((config) => {
  const accountStore = useAccountStore();
  if (accountStore.access_token) {
    config.headers.Authorization = `Bearer ${accountStore.access_token}`;
  }
  return config;
});

instance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const accountStore = useAccountStore();
      accountStore.clearAccountInfo();
      router.push({ name: "signIn" });
    }
    return Promise.reject(error);
  },
);

export default instance;
