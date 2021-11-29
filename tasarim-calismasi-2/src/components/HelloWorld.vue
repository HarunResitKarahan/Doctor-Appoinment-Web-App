<template>
  <div class="hello">
    <table>
      <tr>
        <th>
          Hasta
        </th>
        <template v-for='n in 40' :key="n">
          <th >
            Doktor {{n}}
          </th>
        </template>
      </tr>
      <tr>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>