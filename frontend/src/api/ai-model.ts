import request from "@/utils/request";
import type { AxiosError } from "axios";
import type {
  CreateAiModelRequestSchemas,
  GetAiModelResponseSchemas,
  MessageResponseSchemas,
  UpdateAiModelRequestSchemas,
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

export const testAiModel = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .get(`/ai-model/${id}/test`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "测试模型连接失败！");
    });
};

export const getAiModelById = (id: string): Promise<GetAiModelResponseSchemas> => {
  return request
    .get(`/ai-model/${id}`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取模型信息失败！");
    });
};

export const updateAiModel = (
  id: string,
  data: UpdateAiModelRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/ai-model/${id}`, data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "修改模型失败！");
    });
};

export const deleteAiModel = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .delete(`/ai-model/${id}`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "删除模型失败！");
    });
};
