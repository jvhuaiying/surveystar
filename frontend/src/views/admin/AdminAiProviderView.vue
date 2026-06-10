<script setup lang="ts">
import AdminAiProviderDialog from "@/components/admin/ai-provider/AdminAiProviderDialog.vue";
import AdminAiProviderHeader from "@/components/admin/ai-provider/AdminAiProviderHeader.vue";
import AdminAiProviderTable from "@/components/admin/ai-provider/AdminAiProviderTable.vue";
</script>

<template>
  <div class="p-6 flex-1 h-full flex flex-col justify-center items-center gap-y-6 bg-slate-50">
    <AdminAiProviderHeader />
    <AdminAiProviderTable />
    <AdminAiProviderDialog />
  </div>
</template>
