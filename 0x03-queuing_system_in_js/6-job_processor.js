import { createQueue } from "kue";

const queue = createQueue();

function sendNotification(phonenumber, message){
    console.log(`Sending notification to ${phonenumber}, with message: ${message}`);
}

queue.process('push_notification_code_2', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});

