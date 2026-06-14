<script setup lang="ts">
import { ref, useTemplateRef, watch } from "vue";
import { Delete, Edit, Link } from "@element-plus/icons-vue";
import { deleteAiModel, getAiModelList, testAiModel } from "@/api/ai-model";
import { useElementSize, useWindowSize } from "@vueuse/core";
import { useAiModelDialogStore } from "@/stores/ai-model-dialog";
import { useMutation, useQuery, useQueryCache } from "@pinia/colada";

const showTable = ref(true);
const operating_id = ref("");
const el = useTemplateRef("el");
const { height: height0 } = useElementSize(el);
const { width: width1, height: height1 } = useWindowSize();

const queryCache = useQueryCache();
const dialogStore = useAiModelDialogStore();

const { data, error, isLoading } = useQuery({
  key: ["ai-model-list"],
  query: getAiModelList,
});

const testMutation = useMutation({
  key: ["ai-model-test"],
  mutation: (id: string) => testAiModel(id),
  onSuccess: (data) => {
    ElMessage.success(data.detail);
  },
  onError: (err) => {
    ElMessage.error(err.message);
  },
  onSettled: () => {
    operating_id.value = "";
    queryCache.invalidateQueries({ key: ["ai-model-list"] });
  },
});

const handleTest = (id: string) => {
  operating_id.value = id;
  testMutation.mutate(id);
};

const deleteMutation = useMutation({
  key: ["delete-ai-model"],
  mutation: (id: string) => deleteAiModel(id),
  onSuccess: (data) => ElMessage({ message: data.detail, type: "success" }),
  onError: (err) => ElMessage({ message: (err as Error).message, type: "error" }),
  onSettled: () => {
    operating_id.value = "";
    queryCache.invalidateQueries({ key: ["ai-model-list"] });
  },
});

const handleDelete = (id: string) => {
  ElMessageBox.confirm("确定要删除该模型吗？", "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(() => {
      operating_id.value = id;
      deleteMutation.mutate(id);
    })
    .catch(() => ElMessage({ type: "info", message: "已取消删除" }));
};

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
</script>

<template>
  <div
    class="p-4 w-full flex-1 flex flex-col justify-center items-center bg-slate-200 shadow-md rounded-md"
  >
    <div ref="el" v-loading="isLoading" class="w-full flex-1">
      <el-table :height="height0" v-show="showTable" :data="data" stripe>
        <el-table-column prop="name" label="名称" align="center" />
        <el-table-column prop="api_key" label="API密钥" align="center" width="180">
          <template #default="scope">
            {{ scope.row.api_key.slice(0, 7) + "****" + scope.row.api_key.slice(-4) }}
          </template>
        </el-table-column>
        <el-table-column prop="base_url" label="基础URL" align="center" />
        <el-table-column prop="is_active" label="启用状态" align="center" width="80">
          <template #default="scope">
            <el-tag :type="scope.row.is_active ? 'success' : 'danger'">
              {{ scope.row.is_active ? "启用" : "禁用" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="model_type" label="模型类型" align="center" width="80" />
        <el-table-column prop="test_status" label="测试状态" align="center" width="80">
          <template #default="scope">
            <el-tag
              :type="
                scope.row.test_status === 'untested'
                  ? 'info'
                  : scope.row.test_status === 'success'
                    ? 'success'
                    : 'danger'
              "
            >
              {{
                scope.row.test_status === "untested"
                  ? "待测"
                  : scope.row.test_status === "success"
                    ? "成功"
                    : "失败"
              }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" align="center" width="280">
          <template #default="scope">
            <el-button
              type="primary"
              :icon="Edit"
              :link="true"
              @click="dialogStore.open('edit', scope.row.id)"
            >
              编辑
            </el-button>
            <el-button
              type="primary"
              :icon="Link"
              :link="true"
              @click="handleTest(scope.row.id)"
              :loading="
                operating_id === scope.row.id && testMutation.asyncStatus.value === 'loading'
              "
              :disabled="operating_id !== '' && operating_id !== scope.row.id"
            >
              测试
            </el-button>
            <el-button
              type="danger"
              :icon="Delete"
              :link="true"
              @click="handleDelete(scope.row.id)"
              :loading="
                operating_id === scope.row.id && deleteMutation.asyncStatus.value === 'loading'
              "
              :disabled="operating_id !== '' && operating_id !== scope.row.id"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
