<script setup lang="ts">
import { reactive, ref, watch } from "vue";
import { updateWebsiteInfo } from "@/api/website-info";
import { useMutation, useQueryCache } from "@pinia/colada";
import type { FormInstance, FormRules } from "element-plus";
import type { MessageResponseSchemas } from "@/types/account";
import { Check, RefreshRight } from "@element-plus/icons-vue";
import { getWebsiteInfoUtils } from "@/utils/admin/website-info";
import type { UpdateWebsiteInfoRequestSchemas } from "@/types/website-info";

const queryCache = useQueryCache();
const formRef = ref<FormInstance>();
const { data: websiteInfo } = getWebsiteInfoUtils();

const formModel = reactive<UpdateWebsiteInfoRequestSchemas>({
  name: "",
  description: "",
  icp: null,
});

const rules: FormRules = {
  name: [{ required: true, message: "请输入网站名称", trigger: "blur" }],
  description: [{ required: true, message: "请输入网站描述", trigger: "blur" }],
};

watch(
  websiteInfo,
  (data) => {
    if (!data) return;
    Object.assign(formModel, { name: data.name, description: data.description, icp: data.icp });
  },
  { immediate: true },
);

const { mutate, isLoading } = useMutation({
  key: ["update-website-info"],
  mutation: (data: UpdateWebsiteInfoRequestSchemas) => updateWebsiteInfo(data),
  onSuccess: (data: MessageResponseSchemas) => {
    ElMessage({ message: data.detail, type: "success" });
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["websiteInfo"] }),
});

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate((valid) => {
    if (valid) {
      mutate(formModel);
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
  queryCache.invalidateQueries({ key: ["websiteInfo"] });
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" label-width="auto" class="w-96">
    <el-form-item label="网站名称" prop="name">
      <el-input v-model="formModel.name" placeholder="请输入网站名称" />
    </el-form-item>
    <el-form-item label="网站描述" prop="description">
      <el-input
        v-model="formModel.description"
        type="textarea"
        :rows="3"
        placeholder="请输入网站描述"
      />
    </el-form-item>
    <el-form-item label="ICP备案号" prop="icp">
      <el-input v-model="formModel.icp" placeholder="请输入ICP备案号" />
    </el-form-item>

    <div class="grid grid-cols-2 gap-x-4">
      <el-button type="primary" :icon="Check" :loading="isLoading" @click="submitForm(formRef)"
        >提交</el-button
      >
      <el-button class="ml-0!" type="danger" :icon="RefreshRight" @click="resetForm(formRef)"
        >重置</el-button
      >
    </div>
  </el-form>
</template>
