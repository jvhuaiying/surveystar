<script setup lang="ts">
import { useAccountDialogStore } from "@/stores/account-dialog";
import AdminAccountForm from "@/components/admin/account/AdminAccountForm.vue";
import AdminAccountEditForm from "@/components/admin/account/AdminAccountEditForm.vue";

const dialogStore = useAccountDialogStore();

const handleClose = () => {
  dialogStore.close();
};
</script>

<template>
  <el-dialog
    v-model="dialogStore.visible"
    :before-close="handleClose"
    :show-close="false"
    header-class="p-0!"
    width="420"
    align-center
    destroy-on-close
    body-class="p-6 flex flex-col justify-center items-center gap-y-4"
  >
    <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">
      {{ dialogStore.mode === "create" ? "新增账号" : "编辑账号" }}
    </h1>
    <AdminAccountForm v-show="dialogStore.mode === 'create'" />
    <AdminAccountEditForm v-show="dialogStore.mode === 'edit'" />
  </el-dialog>
</template>
