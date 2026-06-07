<script setup lang="ts">
import { reactive, ref } from "vue";
import { useMutation, useQueryCache } from "@pinia/colada";
import { useAccountDialogStore } from "@/stores/account-dialog";
import { createAccount } from "@/api/account";
import type { FormInstance, FormRules } from "element-plus";
import { Check, Close, Lock, Message, RefreshRight, User } from "@element-plus/icons-vue";
import type { CreateAccountRequestSchemas } from "@/types/account";

const dialogStore = useAccountDialogStore();
const formRef = ref<FormInstance>();
const queryCache = useQueryCache();

const formModel = reactive<CreateAccountRequestSchemas>({
  nickname: "",
  email: "",
  password: "",
  is_active: true,
  kind: "user",
});
const rules: FormRules = {
  nickname: [
    { required: true, message: "请输入昵称", trigger: "blur" },
    { max: 64, message: "昵称最多64个字符", trigger: "blur" },
  ],
  email: [
    { required: true, message: "请输入邮箱地址", trigger: "blur" },
    { type: "email", message: "请输入正确的邮箱地址", trigger: "blur" },
  ],
  password: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 8, message: "密码至少8个字符", trigger: "blur" },
  ],
};

const { mutate, isLoading } = useMutation({
  key: ["create-account"],
  mutation: (data: CreateAccountRequestSchemas) => createAccount(data),
  onSuccess: () => {
    ElMessage({ message: "创建账号成功！", type: "success" });
    formRef.value?.resetFields();
    dialogStore.close();
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["account-list"] }),
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
  <el-form ref="formRef" :model="formModel" :rules="rules" class="w-full">
    <el-form-item prop="nickname">
      <el-input v-model="formModel.nickname" :prefix-icon="User" placeholder="请输入昵称" />
    </el-form-item>
    <el-form-item prop="email">
      <el-input v-model="formModel.email" :prefix-icon="Message" placeholder="请输入邮箱地址" />
    </el-form-item>
    <el-form-item prop="password">
      <el-input
        v-model="formModel.password"
        type="password"
        :prefix-icon="Lock"
        placeholder="请输入密码"
      />
    </el-form-item>
    <div class="flex flex-row justify-between items-center">
      <el-form-item prop="kind">
        <el-radio-group v-model="formModel.kind">
          <el-radio value="user">用户</el-radio>
          <el-radio value="admin">管理员</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item prop="is_active">
        <el-switch v-model="formModel.is_active" active-text="启用" inactive-text="冻结" />
      </el-form-item>
    </div>

    <div class="grid grid-cols-3 gap-x-4">
      <el-button type="primary" :icon="Check" :loading="isLoading" @click="submitForm(formRef)"
        >提交</el-button
      >
      <el-button class="ml-0!" type="danger" :icon="RefreshRight" @click="resetForm(formRef)"
        >重置</el-button
      >
      <el-button class="ml-0!" :icon="Close" @click="closeDialog">关闭</el-button>
    </div>
  </el-form>
</template>
