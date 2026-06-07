<script setup lang="ts">
import dayjs from "dayjs";
import utc from "dayjs/plugin/utc";
import { useQuery } from "@pinia/colada";
import timezone from "dayjs/plugin/timezone";
import { getAccountList } from "@/api/account";
import { ref, useTemplateRef, watch } from "vue";
import { useElementSize, useWindowSize } from "@vueuse/core";

dayjs.extend(utc);
dayjs.extend(timezone);
const showTable = ref(true);
const el = useTemplateRef("el");
const { width: width0, height: height0 } = useWindowSize();
const { height: height1 } = useElementSize(el);

const {
  data: accountList,
  error,
  isLoading,
} = useQuery({
  key: ["account-list"],
  query: getAccountList,
});

watch(error, (err) => {
  if (err) {
    ElMessage({
      message: err.message,
      type: "error",
    });
  }
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
        <el-table-column prop="nickname" label="昵称" align="center" />
        <el-table-column prop="email" label="邮箱" align="center" />
        <el-table-column prop="kind" label="类型" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.kind === 'admin' ? 'success' : 'info'">
              {{ scope.row.kind === "admin" ? "管理员" : "用户" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.status === 'active' ? 'success' : 'danger'">
              {{ scope.row.status === "active" ? "活跃" : "禁用" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="created_at" label="注册时间" align="center" width="180">
          <template #default="scope">
            {{ dayjs.utc(scope.row.created_at).tz("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss") }}
          </template>
        </el-table-column>
        <el-table-column prop="updated_at" label="修改时间" align="center" width="180">
          <template #default="scope">
            {{ dayjs.utc(scope.row.updated_at).tz("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss") }}
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
