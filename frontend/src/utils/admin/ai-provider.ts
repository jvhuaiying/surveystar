import { useQuery } from "@pinia/colada";
import { getAiProviderList } from "@/api/ai-provider";

export const getAiProviderListUtils = () => {
  return useQuery({
    key: ["ai-provider-list"],
    query: getAiProviderList,
  });
};
