<script setup lang="ts">
import { reactive, ref } from "vue";
import { createAiProvider } from "@/api/ai-provider";
import { useMutation, useQueryCache } from "@pinia/colada";
import type { FormInstance, FormRules } from "element-plus";
import { useAiModelDrawerStore } from "@/stores/ai-model-drawer";
import { Check, Close, RefreshRight } from "@element-plus/icons-vue";
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";
import type { CreateAiProviderRequestSchemas, MessageResponseSchemas } from "@/types/ai-provider";

const queryCache = useQueryCache();
const formRef = ref<FormInstance>();
const drawerStore = useAiModelDrawerStore();
const dialogStore = useAiProviderDialogStore();
const prop = defineProps<{ model: "dialog" | "drawer" }>();

const formModel = reactive<CreateAiProviderRequestSchemas>({
  name: "",
  is_active: true,
});

const rules: FormRules = {
  name: [{ required: true, message: "请输入提供商名称", trigger: "blur" }],
};

const { mutate, isLoading } = useMutation({
  key: ["create-ai-provider"],
  mutation: (data: CreateAiProviderRequestSchemas) => createAiProvider(data),
  onSuccess: (data: MessageResponseSchemas) => {
    ElMessage({ message: data.detail, type: "success" });
    switch (prop.model) {
      case "dialog":
        dialogStore.close();
        break;
      case "drawer":
        drawerStore.close();
        break;
    }
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["ai-provider-list"] }),
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
};

const closeDialog = () => {
  switch (prop.model) {
    case "dialog":
      dialogStore.close();
      break;
    case "drawer":
      drawerStore.close();
      break;
  }
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" class="w-full">
    <el-form-item prop="name">
      <el-input v-model="formModel.name" placeholder="请输入提供商名称" />
    </el-form-item>
    <el-form-item label="供应商状态" prop="is_active">
      <el-radio-group v-model="formModel.is_active">
        <el-radio :value="true">启用</el-radio>
        <el-radio :value="false">禁用</el-radio>
      </el-radio-group>
    </el-form-item>

    <div class="grid grid-cols-3 gap-x-4">
      <el-button type="primary" :icon="Check" :loading="isLoading" @click="submitForm(formRef)">
        提交
      </el-button>
      <el-button class="ml-0!" type="danger" :icon="RefreshRight" @click="resetForm(formRef)">
        重置
      </el-button>
      <el-button class="ml-0!" :icon="Close" @click="closeDialog">关闭</el-button>
    </div>
  </el-form>
</template>
