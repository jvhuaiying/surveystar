import { reactive } from "vue";
import { defineStore } from "pinia";
import type { WebsiteInfoResponseSchemas } from "@/types/website-info";

export const useWebsiteInfoStore = defineStore("websiteInfo", () => {
  const websiteInfo = reactive<WebsiteInfoResponseSchemas>({
    id: "",
    logo: "",
    name: "",
    description: "",
    icp: null,
  });

  const setWebsiteInfo = (data: WebsiteInfoResponseSchemas) => {
    Object.assign(websiteInfo, data);
  };

  const clearWebsiteInfo = () => {
    websiteInfo.id = "";
    websiteInfo.logo = "";
    websiteInfo.name = "";
    websiteInfo.description = "";
    websiteInfo.icp = null;
  };

  return { websiteInfo, setWebsiteInfo, clearWebsiteInfo };
});
