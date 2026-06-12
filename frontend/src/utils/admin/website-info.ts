import { useQuery } from "@pinia/colada";
import { getWebsiteInfo } from "@/api/website-info";

export const getWebsiteInfoUtils = () => {
  return useQuery({
    key: ["websiteInfo"],
    query: getWebsiteInfo,
  });
};
