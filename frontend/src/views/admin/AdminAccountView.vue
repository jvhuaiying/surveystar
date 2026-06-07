<script setup lang="ts">
import AdminAccountTable from "@/components/admin/account/AdminAccountTable.vue";
import AdminAccountHeader from "@/components/admin/account/AdminAccountHeader.vue";
import AdminAccountDialog from "@/components/admin/account/AdminAccountDialog.vue";
</script>

<template>
  <div class="p-6 flex-1 h-full flex flex-col justify-center items-center gap-y-6 bg-slate-50">
    <AdminAccountHeader />
    <AdminAccountTable />
    <AdminAccountDialog />
  </div>
</template>
