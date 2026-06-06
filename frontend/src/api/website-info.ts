import request from "@/utils/request";
import type { WebsiteInfoResponseSchemas } from "@/types/website-info";

export const getWebsiteInfo = (): Promise<WebsiteInfoResponseSchemas> => {
  return request
    .get<WebsiteInfoResponseSchemas>("/website-info/")
    .then((res) => res.data)
    .catch((err) => {
      throw err;
    });
};
