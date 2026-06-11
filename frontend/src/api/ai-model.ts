import request from "@/utils/request";
import type { AxiosError } from "axios";
import type {
  CreateAiModelRequestSchemas,
  GetAiModelResponseSchemas,
  MessageResponseSchemas,
} from "@/types/ai-model";

export const createAiModel = (
  data: CreateAiModelRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .post("/ai-model/", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "创建模型失败！");
    });
};

export const getAiModelList = (): Promise<GetAiModelResponseSchemas[]> => {
  return request
    .get("/ai-model/")
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取模型列表失败！");
    });
};
