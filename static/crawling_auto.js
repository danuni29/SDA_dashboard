// 잘 돌아가는지 확인할 방법이 없음 ( 나중에 확인시도 )

const schedule = require('node-schedule');
const { exec } = require('child_process');

// 실행할 날짜와 시간 설정
const scheduledDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
scheduledDate.setDate(scheduledDate.getDate() + (1 + 7 - scheduledDate.getDay()) % 7); // 다음 월요일 계산

// 스케줄링 작업 설정
const job = schedule.scheduleJob(scheduledDate, function () {
  // 파이썬 스크립트 실행
  const pythonScript = 'C:\\code\\SDA_dashboard\\main.py'; // 파이썬 스크립트 경로
  exec(`python ${pythonScript}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error}`);
    } else {
      console.log(`Python script executed successfully:\n${stdout}`);
    }
  });
});

console.log(`Scheduled Python script execution for: ${scheduledDate}`);
