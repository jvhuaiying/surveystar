<script setup lang="ts">
import { reactive, ref, onMounted, watch } from "vue";
import { getAiModelById, updateAiModel } from "@/api/ai-model";
import { useMutation, useQueryCache } from "@pinia/colada";
import type { FormInstance, FormRules } from "element-plus";
import { useAiModelDialogStore } from "@/stores/ai-model-dialog";
import { useAiModelDrawerStore } from "@/stores/ai-model-drawer";
import { getAiProviderListUtils } from "@/utils/admin/ai-provider";
import { Check, Close, Plus, RefreshRight } from "@element-plus/icons-vue";
import type { MessageResponseSchemas, UpdateAiModelRequestSchemas } from "@/types/ai-model";

const formRef = ref<FormInstance>();
const queryCache = useQueryCache();
const dialogStore = useAiModelDialogStore();
const drawerStore = useAiModelDrawerStore();

const formModel = reactive<UpdateAiModelRequestSchemas>({
  name: "",
  api_key: "",
  base_url: "",
  is_active: true,
  model_type: "",
  provider_id: "",
});

const rules: FormRules = {
  name: [{ required: true, message: "请输入模型名称", trigger: "blur" }],
  api_key: [{ required: true, message: "请输入API密钥", trigger: "blur" }],
  base_url: [{ required: true, message: "请输入基础URL", trigger: "blur" }],
  model_type: [{ required: true, message: "请输入模型类型", trigger: "blur" }],
  provider_id: [{ required: true, message: "请选择供应商", trigger: "change" }],
};

const { data: providerList, error: err0, isLoading: load0 } = getAiProviderListUtils();

watch(err0, (err) => {
  if (err) {
    ElMessage({
      message: err.message,
      type: "error",
    });
  }
});

const { mutate: fetchModel, isLoading: isFetching } = useMutation({
  key: (id: string) => ["ai-model", id],
  mutation: (id: string) => getAiModelById(id),
  onSuccess: (model) => {
    formModel.name = model.name;
    formModel.api_key = model.api_key;
    formModel.base_url = model.base_url;
    formModel.is_active = model.is_active;
    formModel.model_type = model.model_type;
    formModel.provider_id = model.provider_id;
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
    dialogStore.close();
  },
});

onMounted(() => {
  if (dialogStore.currentId) {
    fetchModel(dialogStore.currentId);
  }
});

const { mutate: submitModel, isLoading: isSubmitting } = useMutation({
  key: ["update-ai-model"],
  mutation: (vars: { id: string; data: UpdateAiModelRequestSchemas }) =>
    updateAiModel(vars.id, vars.data),
  onSuccess: (data: MessageResponseSchemas) => {
    ElMessage({ message: data.detail, type: "success" });
    dialogStore.close();
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["ai-model-list"] }),
});

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate((valid) => {
    if (valid) {
      submitModel({ id: dialogStore.currentId!, data: formModel });
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
  fetchModel(dialogStore.currentId!);
};

const closeDialog = () => {
  dialogStore.close();
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" class="w-full" v-loading="isFetching || load0">
    <el-form-item prop="provider_id">
      <div class="w-full flex flex-row justify-center items-center gap-x-2">
        <el-select v-model="formModel.provider_id" placeholder="请选择供应商" class="flex-1">
          <el-option
            v-for="item in providerList ?? []"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
        <el-button :icon="Plus" type="primary" @click="drawerStore.open('create', null)" />
      </div>
    </el-form-item>
    <el-form-item prop="name">
      <el-input v-model="formModel.name" placeholder="请输入模型名称" />
    </el-form-item>
    <el-form-item prop="api_key">
      <el-input
        v-model="formModel.api_key"
        type="password"
        placeholder="请输入API密钥"
        show-password
      />
    </el-form-item>
    <el-form-item prop="base_url">
      <el-input v-model="formModel.base_url" placeholder="请输入基础URL" />
    </el-form-item>
    <el-form-item prop="model_type">
      <el-input v-model="formModel.model_type" placeholder="请输入模型类型" />
    </el-form-item>
    <el-form-item label="模型状态" prop="is_active">
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
