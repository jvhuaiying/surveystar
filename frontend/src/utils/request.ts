import axios from "axios";
import { useAccountStore } from "@/stores/account";

const instance = axios.create({
  baseURL: "/api",
});

instance.interceptors.request.use((config) => {
  const accountStore = useAccountStore();
  if (accountStore.accountInfo.access_token) {
    config.headers.Authorization = `Bearer ${accountStore.accountInfo.access_token}`;
  }
  return config;
});

export default instance;
