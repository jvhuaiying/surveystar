<script setup lang="ts">
import AdminAiModelDialog from "@/components/admin/ai-model/AdminAiModelDialog.vue";
import AdminAiModelHeader from "@/components/admin/ai-model/AdminAiModelHeader.vue";
import AdminAiModelTable from "@/components/admin/ai-model/AdminAiModelTable.vue";
import AdminAiModelDrawer from "@/components/admin/ai-model/AdminAiModelDrawer.vue";
</script>

<template>
  <div class="p-6 flex-1 h-full flex flex-col justify-center items-center gap-y-6 bg-slate-50">
    <AdminAiModelHeader />
    <AdminAiModelTable />
    <AdminAiModelDialog />
    <AdminAiModelDrawer />
  </div>
</template>
