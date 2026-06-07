<script setup lang="ts">
import { getAccountList } from "@/api/account";
import { onMounted, ref, useTemplateRef, watch } from "vue";
import { useElementSize, useWindowSize } from "@vueuse/core";
import type { GetAccountListResponseSchemas } from "@/types/account";

const showTable = ref(true);
const isLoading = ref(true);
const el = useTemplateRef("el");
const { width: width0, height: height0 } = useWindowSize();
const { height: height1 } = useElementSize(el);
const accountList = ref<GetAccountListResponseSchemas[]>([]);

onMounted(() => {
  getAccountList()
    .then((res) => {
      accountList.value = res;
    })
    .catch((err) => {
      ElMessage({
        message: err.response?.data.detail || "登录失败！",
        type: "error",
      });
    })
    .finally(() => {
      isLoading.value = false;
    });
});

watch([width0, height0], () => {
  showTable.value = false;
  setTimeout(() => {
    showTable.value = true;
  }, 100);
});
</script>

<template>
  <div
    class="p-4 w-full flex-1 flex flex-col justify-center items-center bg-slate-200 shadow-md rounded-md"
  >
    <div ref="el" v-loading="isLoading" class="w-full flex-1">
      <el-table :height="height1" v-show="showTable" :data="accountList" stripe>
        <el-table-column prop="nickname" label="昵称" />
        <el-table-column prop="email" label="邮箱" />
        <el-table-column prop="kind" label="类型" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.kind === 'admin' ? 'success' : 'info'">
              {{ scope.row.kind === "admin" ? "管理员" : "用户" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="is_active" label="状态" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.is_active ? 'success' : 'danger'">
              {{ scope.row.is_active ? "正常" : "冻结" }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
