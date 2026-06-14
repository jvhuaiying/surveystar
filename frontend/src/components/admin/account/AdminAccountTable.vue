<script setup lang="ts">
import { ref, useTemplateRef, watch } from "vue";
import { useElementSize, useWindowSize } from "@vueuse/core";
import { useAccountDialogStore } from "@/stores/account-dialog";
import { useMutation, useQuery, useQueryCache } from "@pinia/colada";
import { Check, Delete, Remove, Edit } from "@element-plus/icons-vue";
import { activateAccount, deleteAccount, disableAccount, getAccountList } from "@/api/account";

const showTable = ref(true);
const el = useTemplateRef("el");
const queryCache = useQueryCache();
const dialogStore = useAccountDialogStore();
const { height: height0 } = useElementSize(el);
const { width: width1, height: height1 } = useWindowSize();

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

watch([width1, height1], () => {
  showTable.value = false;
  setTimeout(() => {
    showTable.value = true;
  }, 100);
});

const { mutate: mutateDisable } = useMutation({
  key: ["disable-account"],
  mutation: (id: string) => disableAccount(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: (err as Error).message, type: "error" }),
  onSettled: () => queryCache.invalidateQueries({ key: ["account-list"] }),
});

const { mutate: mutateActivate } = useMutation({
  key: ["activate-account"],
  mutation: (id: string) => activateAccount(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: err.message, type: "error" }),
  onSettled: () => queryCache.invalidateQueries({ key: ["account-list"] }),
});

const { mutate: mutateDelete } = useMutation({
  key: ["delete-account"],
  mutation: (id: string) => deleteAccount(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: err.message, type: "error" }),
  onSettled: () => queryCache.invalidateQueries({ key: ["account-list"] }),
});

const handleDisable = (id: string) => mutateDisable(id);

const handleActivate = (id: string) => mutateActivate(id);

const handleDelete = (id: string) => {
  ElMessageBox.confirm("确定要删除该账号吗？此操作不可恢复！", "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "warning",
  }).then(() => {
    mutateDelete(id);
  });
};

const handleEdit = (id: string) => {
  dialogStore.open("edit", id);
};
</script>

<template>
  <div
    class="p-4 w-full flex-1 flex flex-col justify-center items-center bg-slate-200 shadow-md rounded-md"
  >
    <div ref="el" v-loading="isLoading" class="w-full flex-1">
      <el-table :height="height0" v-show="showTable" :data="accountList" stripe>
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
        <el-table-column label="操作" align="center" width="240">
          <template #default="scope">
            <el-button type="success" size="small" :icon="Edit" @click="handleEdit(scope.row.id)">
              编辑
            </el-button>
            <el-button
              v-if="scope.row.status === 'active'"
              type="warning"
              size="small"
              :icon="Remove"
              @click="handleDisable(scope.row.id)"
            >
              禁用
            </el-button>
            <el-button
              v-if="scope.row.status === 'disabled'"
              type="primary"
              size="small"
              :icon="Check"
              @click="handleActivate(scope.row.id)"
            >
              激活
            </el-button>
            <el-button
              type="danger"
              size="small"
              :icon="Delete"
              @click="handleDelete(scope.row.id)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
