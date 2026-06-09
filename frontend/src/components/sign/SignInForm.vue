<script setup lang="ts">
import { reactive, ref } from "vue";
import { signin } from "@/api/account";
import { useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import type { FormInstance, FormRules } from "element-plus";
import type { SigninRequestSchemas } from "@/types/account";
import { Lock, Message, Promotion, RefreshRight, Right } from "@element-plus/icons-vue";

const router = useRouter();
const formRef = ref<FormInstance>();
const accountStore = useAccountStore();
const formModel = reactive<SigninRequestSchemas>({
  email: "",
  password: "",
  kind: "user",
  remember: false,
});
const rules: FormRules = {
  email: [
    { required: true, message: "请输入邮箱地址", trigger: "blur" },
    { type: "email", message: "请输入正确的邮箱地址", trigger: "blur" },
  ],
  password: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 8, message: "密码至少8个字符", trigger: "blur" },
  ],
};

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate((valid) => {
    if (valid) {
      signin(formModel)
        .then((res) => {
          accountStore.setAccountInfo(res);
          ElMessage({
            message: "登录成功！",
            type: "success",
          });
          if (accountStore.accountInfo.kind === "admin") {
            router.push({ name: "adminWebInfo" });
          }
        })
        .catch((err: Error) => {
          ElMessage({
            message: err.message,
            type: "error",
          });
        });
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>

<template>
  <el-form ref="formRef" :model="formModel" :rules="rules" label-width="auto" class="w-full">
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
    <el-form-item>
      <el-radio-group v-model="formModel.kind">
        <el-radio value="user">用户</el-radio>
        <el-radio value="admin">管理员</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item>
      <div class="w-full flex flex-row justify-between items-center">
        <el-checkbox v-model="formModel.remember">记住我</el-checkbox>
        <el-link type="primary" underline="never">忘记密码？</el-link>
      </div>
    </el-form-item>
    <div class="grid grid-cols-3 gap-4">
      <el-button type="primary" :icon="Promotion" @click="submitForm(formRef)">登录</el-button>
      <el-button class="ml-0!" type="danger" :icon="RefreshRight" @click="resetForm(formRef)"
        >重置</el-button
      >
      <el-button class="ml-0!" type="success" :icon="Right">前往注册</el-button>
    </div>
  </el-form>
</template>
