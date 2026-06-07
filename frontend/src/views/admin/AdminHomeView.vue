<script setup lang="ts">
import { RouterView } from "vue-router";
import AdminHeader from "@/components/admin/AdminHeader.vue";
import AdminSideMenu from "@/components/admin/AdminSideMenu.vue";
</script>

<template>
  <div class="w-full h-screen flex flex-col justify-start items-center">
    <AdminHeader />
    <div class="w-full flex-1 flex flex-row justify-start items-center">
      <AdminSideMenu />
      <RouterView />
    </div>
  </div>
</template>
