<script setup lang="ts">
import AdminPromptDialog from "@/components/admin/prompt/AdminPromptDialog.vue";
import AdminPromptHeader from "@/components/admin/prompt/AdminPromptHeader.vue";
import AdminPromptTable from "@/components/admin/prompt/AdminPromptTable.vue";
</script>

<template>
  <div class="p-6 flex-1 h-full flex flex-col justify-center items-center gap-y-6 bg-slate-50">
    <AdminPromptHeader />
    <AdminPromptTable />
    <AdminPromptDialog />
  </div>
</template>
