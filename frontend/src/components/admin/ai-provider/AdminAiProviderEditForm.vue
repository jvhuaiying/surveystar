<script setup lang="ts">
import { reactive, ref, onMounted } from "vue";
import { getAiProviderById, updateAiProvider } from "@/api/ai-provider";
import { useMutation, useQueryCache } from "@pinia/colada";
import type { FormInstance, FormRules } from "element-plus";
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";
import type { MessageResponseSchemas, UpdateAiProviderRequestSchemas } from "@/types/ai-provider";
import { Check, Close, RefreshRight } from "@element-plus/icons-vue";

const formRef = ref<FormInstance>();
const queryCache = useQueryCache();
const dialogStore = useAiProviderDialogStore();

const formModel = reactive<UpdateAiProviderRequestSchemas>({
  name: "",
  is_active: true,
});

const rules: FormRules = {
  name: [{ required: true, message: "请输入提供商名称", trigger: "blur" }],
};

const { mutate: fetchProvider, isLoading: isFetching } = useMutation({
  key: (id: string) => ["ai-provider", id],
  mutation: (id: string) => getAiProviderById(id),
  onSuccess: (provider) => {
    formModel.name = provider.name;
    formModel.is_active = provider.is_active;
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
    dialogStore.close();
  },
});

onMounted(() => {
  if (dialogStore.currentId) {
    fetchProvider(dialogStore.currentId);
  }
});

const { mutate: submitProvider, isLoading: isSubmitting } = useMutation({
  key: ["update-ai-provider"],
  mutation: (vars: { id: string; data: UpdateAiProviderRequestSchemas }) =>
    updateAiProvider(vars.id, vars.data),
  onSuccess: (data: MessageResponseSchemas) => {
    ElMessage({ message: data.detail, type: "success" });
    dialogStore.close();
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
      submitProvider({ id: dialogStore.currentId!, data: formModel });
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
  fetchProvider(dialogStore.currentId!);
};

const closeDialog = () => {
  dialogStore.close();
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" class="w-full" v-loading="isFetching">
    <el-form-item prop="name">
      <el-input v-model="formModel.name" placeholder="请输入提供商名称" />
    </el-form-item>
    <el-form-item prop="is_active">
      <el-radio-group v-model="formModel.is_active">
        <el-radio :value="true">启用</el-radio>
        <el-radio :value="false">禁用</el-radio>
      </el-radio-group>
    </el-form-item>

    <div class="grid grid-cols-3 gap-x-4">
      <el-button type="primary" :icon="Check" :loading="isSubmitting" @click="submitForm(formRef)">
        提交
      </el-button>
      <el-button class="ml-0!" type="danger" :icon="RefreshRight" @click="resetForm(formRef)">
        重置
      </el-button>
      <el-button class="ml-0!" :icon="Close" @click="closeDialog">关闭</el-button>
    </div>
  </el-form>
</template>
