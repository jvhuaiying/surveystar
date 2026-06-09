import request from "@/utils/request";
import type { AxiosError } from "axios";
import type {
  UpdateWebsiteInfoRequestSchemas,
  WebsiteInfoResponseSchemas,
} from "@/types/website-info";
import type { MessageResponseSchemas } from "@/types/account";

export const getWebsiteInfo = (): Promise<WebsiteInfoResponseSchemas> => {
  return request
    .get<WebsiteInfoResponseSchemas>("/website-info/")
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取网站信息失败！");
    });
};

export const updateWebsiteInfo = (
  data: UpdateWebsiteInfoRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .put<MessageResponseSchemas>("/website-info/", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "更新网站信息失败！");
    });
};

export const updateWebsiteLogo = async (logo: File): Promise<MessageResponseSchemas> => {
  const res = await request.postForm("/website-info/logo/", {
    logo,
  });
  return res.data;
};
