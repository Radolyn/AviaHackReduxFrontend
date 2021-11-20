<template>
  <center>
    <div class='card'>
      <br>
      <img src='../static/gear.png' class='gear'>
      <br>
      <div>
        <div class='profile-module'>
            <span>
              Фамилия Имя Отчество
            </span>
        </div>
        <div class='profile-module-content'>
              <span>
                {{ name }}
              </span>
        </div>
      </div>
      <br>

      <div>
        <div class='profile-module'>
            <span>
              Паспорт
            </span>
        </div>
        <div class='profile-module-content'>
              <span>
                {{ passport }}
              </span>
        </div>
      </div>

      <br><br><br><br><br>

      <div>
         <span>
          Есть несоответствия?
        </span>
      </div>
      <div>
        <span class='active-turner px-2 py-1'>
          helpdesk@radolyn.com
        </span>
      </div>

    </div>
  </center>
</template>

<script>

export default {
  data() {
    return {
      name : 'Киселева Елена Мразотовна',
      passport : '## ## ######'
    }
  },
  mounted() {
    // fetch name and passport from server
  }
}

</script>
