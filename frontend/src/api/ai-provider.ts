import request from "@/utils/request";
import type { AxiosError } from "axios";
import type {
  CreateAiProviderRequestSchemas,
  GetAiProviderResponseSchemas,
  MessageResponseSchemas,
  UpdateAiProviderRequestSchemas,
} from "@/types/ai-provider";

export const createAiProvider = (
  data: CreateAiProviderRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .post("/ai-provider/", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "创建提供商失败！");
    });
};

export const getAiProviderList = (): Promise<GetAiProviderResponseSchemas[]> => {
  return request
    .get("/ai-provider/")
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取提供商列表失败！");
    });
};

export const disableAiProvider = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/ai-provider/${id}/disable`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "禁用提供商失败！");
    });
};

export const activateAiProvider = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/ai-provider/${id}/activate`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "启用提供商失败！");
    });
};

export const getAiProviderById = (id: string): Promise<GetAiProviderResponseSchemas> => {
  return request
    .get(`/ai-provider/${id}`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取提供商信息失败！");
    });
};

export const updateAiProvider = (
  id: string,
  data: UpdateAiProviderRequestSchemas,
): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/ai-provider/${id}`, data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "修改提供商失败！");
    });
};

export const deleteAiProvider = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .delete(`/ai-provider/${id}`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "删除提供商失败！");
    });
};
