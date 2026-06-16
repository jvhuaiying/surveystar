import request from "@/utils/request";
import type { AxiosError } from "axios";
import type {
  CreateSystemPromptRequestSchemas,
  GetSystemPromptResponseSchemas,
  MessageResponseSchemas,
} from "@/types/prompt";

export const createSystemPrompt = (
  data: CreateSystemPromptRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .post("/prompt/", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "创建提示词失败！");
    });
};

export const getSystemPromptList = (): Promise<GetSystemPromptResponseSchemas[]> => {
  return request
    .get("/prompt/")
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取提示词列表失败！");
    });
};
