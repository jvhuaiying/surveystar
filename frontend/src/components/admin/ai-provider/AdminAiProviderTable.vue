<script setup lang="ts">
import dayjs from "dayjs";
import utc from "dayjs/plugin/utc";
import timezone from "dayjs/plugin/timezone";
import { ref, useTemplateRef, watch } from "vue";
import { useElementSize, useWindowSize } from "@vueuse/core";
import { useMutation, useQuery, useQueryCache } from "@pinia/colada";
import { Check, Delete, Edit, Remove } from "@element-plus/icons-vue";
import {
  activateAiProvider,
  deleteAiProvider,
  disableAiProvider,
  getAiProviderList,
} from "@/api/ai-provider";
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";

dayjs.extend(utc);
dayjs.extend(timezone);
const showTable = ref(true);
const el = useTemplateRef("el");
const { height: height0 } = useElementSize(el);
const { width: width1, height: height1 } = useWindowSize();

const {
  data: providerList,
  error,
  isLoading,
} = useQuery({
  key: ["ai-provider-list"],
  query: getAiProviderList,
});

watch(error, (err) => {
  if (err) {
    ElMessage({
      message: err.message,
      type: "error",
    });
  }
});

const queryCache = useQueryCache();

const { mutate: mutateDisable } = useMutation({
  key: ["disable-ai-provider"],
  mutation: (id: string) => disableAiProvider(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: (err as Error).message, type: "error" }),
  onSettled: () => queryCache.invalidateQueries({ key: ["ai-provider-list"] }),
});

const { mutate: mutateActivate } = useMutation({
  key: ["activate-ai-provider"],
  mutation: (id: string) => activateAiProvider(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: err.message, type: "error" }),
  onSettled: () => queryCache.invalidateQueries({ key: ["ai-provider-list"] }),
});

const { mutate: mutateDelete } = useMutation({
  key: ["delete-ai-provider"],
  mutation: (id: string) => deleteAiProvider(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: (err as Error).message, type: "error" }),
  onSettled: () => {
    queryCache.invalidateQueries({ key: ["ai-provider-list"] });
    queryCache.invalidateQueries({ key: ["ai-model-list"] });
  },
});

const dialogStore = useAiProviderDialogStore();

const handleDisable = (id: string) => mutateDisable(id);

const handleActivate = (id: string) => mutateActivate(id);

const handleEdit = (id: string) => {
  dialogStore.open("edit", id);
};

const handleDelete = (id: string) => {
  ElMessageBox.confirm(
    "确定要删除该供应商吗？此操作将同时删除其下所有模型，且不可恢复。",
    "警告",
    {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning",
    },
  )
    .then(() => {
      mutateDelete(id);
    })
    .catch(() => {
      ElMessage({ type: "info", message: "已取消删除" });
    });
};

watch([width1, height1], () => {
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
      <el-table :height="height0" v-show="showTable" :data="providerList" stripe>
        <el-table-column prop="name" label="名称" align="center" />
        <el-table-column prop="is_active" label="状态" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.is_active ? 'success' : 'danger'">
              {{ scope.row.is_active ? "启用" : "禁用" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="created_at" label="创建时间" align="center" width="180">
          <template #default="scope">
            {{ dayjs.utc(scope.row.created_at).tz("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss") }}
          </template>
        </el-table-column>
        <el-table-column prop="updated_at" label="修改时间" align="center" width="180">
          <template #default="scope">
            {{ dayjs.utc(scope.row.updated_at).tz("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss") }}
          </template>
        </el-table-column>
        <el-table-column label="操作" align="center" width="360">
          <template #default="scope">
            <el-button
              type="primary"
              size="small"
              :icon="Edit"
              @click="handleEdit(scope.row.id)"
            >
              编辑
            </el-button>
            <el-button
              v-if="scope.row.is_active"
              type="warning"
              size="small"
              :icon="Remove"
              @click="handleDisable(scope.row.id)"
            >
              禁用
            </el-button>
            <el-button
              v-else
              type="primary"
              size="small"
              :icon="Check"
              @click="handleActivate(scope.row.id)"
            >
              启用
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
