<script setup lang="ts">
import { ref, useTemplateRef, watch } from "vue";
import { useQuery } from "@pinia/colada";
import { getSystemPromptList } from "@/api/prompt";
import { useDebounceFn, useElementSize, useWindowSize } from "@vueuse/core";

const showTable = ref(true);
const el = useTemplateRef("el");
const { height: height0 } = useElementSize(el);
const { width: width1, height: height1 } = useWindowSize();

const { data, error, isLoading } = useQuery({
  key: ["system-prompt-list"],
  query: getSystemPromptList,
});

watch(error, (err) => {
  if (err) {
    ElMessage({ message: err.message, type: "error" });
  }
});

const debouncedFn = useDebounceFn(() => {
  showTable.value = true;
}, 100);

watch([width1, height1], () => {
  showTable.value = false;
  debouncedFn();
});
</script>

<template>
  <div
    class="p-4 w-full flex-1 flex flex-col justify-center items-center bg-slate-200 shadow-md rounded-md"
  >
    <div ref="el" v-loading="isLoading || !showTable" class="w-full flex-1">
      <el-table :height="height0" v-show="showTable" :data="data" stripe>
        <el-table-column prop="content" label="提示词内容" align="center" />
        <el-table-column prop="is_active" label="启用状态" align="center" width="100">
          <template #default="scope">
            <el-tag :type="scope.row.is_active ? 'success' : 'danger'">
              {{ scope.row.is_active ? "启用" : "禁用" }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="所属账号" align="center" width="200">
          <template #default="scope">
            {{ scope.row.account_nickname }}
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
