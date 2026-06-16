<script setup lang="ts">
import { reactive, ref, watch } from "vue";
import { createSystemPrompt } from "@/api/prompt";
import { getAccountList } from "@/api/account";
import { useMutation, useQuery, useQueryCache } from "@pinia/colada";
import type { FormInstance, FormRules } from "element-plus";
import { usePromptDialogStore } from "@/stores/prompt-dialog";
import { Check, Close, RefreshRight } from "@element-plus/icons-vue";
import type { CreateSystemPromptRequestSchemas } from "@/types/prompt";

const queryCache = useQueryCache();
const formRef = ref<FormInstance>();
const dialogStore = usePromptDialogStore();

const formModel = reactive<CreateSystemPromptRequestSchemas>({
  content: "",
  is_active: true,
  account_id: "",
});

const rules: FormRules = {
  content: [{ required: true, message: "请输入提示词内容", trigger: "blur" }],
  account_id: [{ required: true, message: "请选择所属账号", trigger: "change" }],
};

const {
  data: accountList,
  error: err0,
  isLoading: load0,
} = useQuery({
  key: ["account-list"],
  query: getAccountList,
});

watch(err0, (err) => {
  if (err) {
    ElMessage({ message: err.message, type: "error" });
  }
});

const { mutate, isLoading } = useMutation({
  key: ["create-system-prompt"],
  mutation: (data: CreateSystemPromptRequestSchemas) => createSystemPrompt(data),
  onSuccess: (data) => {
    ElMessage({ message: data.detail, type: "success" });
    dialogStore.close();
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["system-prompt-list"] }),
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
  dialogStore.close();
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" class="w-full" v-loading="load0">
    <el-form-item prop="content">
      <el-input
        v-model="formModel.content"
        placeholder="请输入提示词内容"
        type="textarea"
        :rows="12"
      />
    </el-form-item>
    <el-form-item prop="account_id">
      <el-select v-model="formModel.account_id" placeholder="请选择所属账号" class="w-full">
        <el-option
          v-for="item in accountList ?? []"
          :key="item.id"
          :label="item.nickname + ' (' + item.email + ')'"
          :value="item.id"
        />
      </el-select>
    </el-form-item>
    <el-form-item prop="is_active">
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
